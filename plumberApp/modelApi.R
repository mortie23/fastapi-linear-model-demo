#!/usr/bin/env Rscript

library(plumber)
r <- plumb('model.R')
r$run(host="127.0.0.1", port=8000, swagger=TRUE)