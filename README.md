---
title: "Tree"
output: html_notebook
---

```{r}
# For manipulating the datasets
library(dplyr)
library(readr)
# For plotting correlation matrix
library(ggcorrplot)
# Machine Learning library
library(caret)
# For Multi-core processing support
library(doParallel)

```
# GET THE DATA
## Load the datasets


```{r}
treedataset <- read_csv("data/arbolado-mza-dataset.csv")
treedataset<-rbind(treedataset)
# Print the dataset
#treedataset

```

# TRAIN THE MODEL
## Split train and test
```{r}

trainset <- treedataset
trainIndex <- createDataPartition(as.factor(trainset$inclinacion_peligrosa), p=0.80, list=FALSE)
data_train <- trainset[ trainIndex,]
data_test <-  trainset[-trainIndex,]
colnames(data_train) <- make.names(colnames(data_train))
colnames(data_test) <- make.names(colnames(data_test))
data_train$inclinacion_peligrosa <- as.factor(data_train$inclinacion_peligrosa)
data_test$inclinacion_peligrosa <- as.factor(data_test$inclinacion_peligrosa)


x <- data_train %>% filter(inclinacion_peligrosa == 0) %>% sample_n(4500)
y <- data_train %>% filter(inclinacion_peligrosa == 1)

d<- rbind(x,y)


```

```{r}
data_testFin <-  readr::read_csv("./arbolado-mza-dataset-test.csv",col_types = cols(
  id = col_integer(),
  especie = col_character(),
  ultima_modificacion = col_character(),
  altura = col_character(),
  circ_tronco_cm = col_double(),
  diametro_tronco = col_character(),
  long = col_double(),
  lat = col_double(),
  seccion = col_integer(),
  nombre_seccion = col_character(),
  area_seccion = col_double()
))
```
## Train model
```{r}

ctrl_fast <- trainControl(method="cv", 
                       number=12, 
                       verboseIter=T,
                     classProbs=F,
                     allowParallel = TRUE
                  
                     )  
```
```{r}
registerDoParallel(cores=8)
train_formula<-formula(inclinacion_peligrosa~especie+long+lat+seccion+diametro_tronco)

rfFitupsam<- train(train_formula,
               data = d,
               tuneLength=20,
               #method="rpart",
               #method="rf",
               method = "rf",
               #preProcess=c("scale","center"),
               metric = "Kappa",
               trControl = ctrl_fast)

rfFitupsam


```



# TEST THE DATA
```{r}
predsrfprobsamp=predict(rfFitupsam,data_test)
as.data.frame(predsrfprobsamp)

confusionMatrix(predsrfprobsamp,as.factor(data_test$inclinacion_peligrosa))
```


```{r}
preds_tree_probs=predict(rfFitupsam,data_testFin,type='prob')
head(preds_tree_probs)
```

```{r}
preds_tree=ifelse(preds_tree_probs[,2] >=0.5,1,0)
head(preds_tree)
```


```{r}
submission<-data.frame(id=data_testFin$id,inclinacion_peligrosa=preds_tree)
readr::write_csv(submission,"./arbolado-mza-dataset-envio-ejemplo-rpart15.csv")
head(submission)
```

