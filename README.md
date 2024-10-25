# Financial Analysis and Modeling

This project focuses on financial analysis using advanced statistical techniques, including volatility modeling, kriging interpolation, and the use of Gaussian processes.

## Table of Contents

1. [Introduction](#introduction)
2. [Analysis using GARCH Processes](#analysis-using-garch-processes)
3. [Gaussian Processes and Kriging Interpolation](#gaussian-processes-and-kriging-interpolation)
4. [Modeling with Copulas](#modeling-with-copulas)
5. [Extreme Value Analysis](#extreme-value-analysis)
6. [Bibliography](#bibliography)

## Introduction

This project explores statistical models for analyzing the returns of financial assets, focusing on risk management and volatility forecasting. We use GARCH models to model conditional volatility and Gaussian processes for data interpolation.

## Analysis using GARCH Processes

### ARCH and GARCH Models

We introduced ARCH (Autoregressive Conditional Heteroskedasticity) and GARCH (Generalized Autoregressive Conditional Heteroskedasticity) models to model asset returns while accounting for volatility. The GARCH(1,1) model was fitted, with significant results indicating volatility dependence on past returns.

### McLeod-Li Test

We performed the McLeod-Li test to detect the presence of ARCH effects in the residuals, with results suggesting significant effects, leading us to continue our analysis with the GARCH model.

### Fitting the GARCH(P,Q) Model

Fitting the GARCH model yielded predictive parameters that capture the volatility structure. We observed that the model is effective in the short term but less reliable for long-term forecasts.

### Volatility Forecasting

We explored two volatility forecasting methods:
1. **N-Step Ahead Forecasting**: Limited to short-term forecasts.
2. **One-Step Ahead Real-Time Forecasting**: Updating the model daily for more reliable forecasts.

### Model Evaluation

The Jarque-Bera test was applied to check the normality of the model's errors, and results indicated the need to explore more suitable distributions, such as the Student's t-distribution.

![GARCH(1,1) Model - Results Visualization](figures/GARCH.png)

## Gaussian Processes and Kriging Interpolation

### Gaussian Process

We defined a Gaussian random vector and discussed the importance of kernel choice for the covariance function. We used the Matern kernel to capture spatial dependence in the data.

### Kriging with Gaussian Processes

Kriging was used to make predictions from known data. We showed that this method is suitable for estimating intermediate values.

### Maximum Likelihood Estimation

We maximized the likelihood function to calibrate our model and capture the spatial dependence structure.

### Application to Our Data

We applied kriging to predict stock prices from hourly values, generating a 95% confidence interval.

![Gaussian Process Kriging Model - Results Visualization](figures/gaussianprocesses.png)

## Modeling with Copulas

The `copulas.ipynb` notebook implements copula models to analyze dependencies between financial assets. Copulas allow us to capture complex relationships between variables that cannot be fully explained by correlation alone. In this notebook, we explore various types of copulas (such as Gaussian and t-Copulas) and their applications in risk management and portfolio optimization.

### Key Steps:
- Load financial data and preprocess it.
- Fit different copula models to the data.
- Analyze the results and visualize the dependency structures.

![Copulas Model - Results Visualization](figures/copulas.png)

## Extreme Value Analysis

The extreme value analysis is conducted in the relevant notebooks to assess the behavior of financial time series in the tails of the distribution. This is crucial for understanding the likelihood of extreme events, such as market crashes or unexpected surges.

### Key Steps:
- Apply extreme value theory (EVT) to financial data.
- Estimate the parameters of the extreme value distribution.
- Conduct simulations to predict the probability of extreme losses or gains.

By studying extreme values, we can better manage risk and prepare for potential market volatility.

![Extreme Value Theory - Results Visualization 1](figures/extremevalues1.png)
![Extreme Value Theory - Results Visualization 2](figures/extremevalues2.png)

## Structure of the Repository

The structure is:

```bash
├── GARCH.ipynb
├── LICENSE
├── MAP_565_report.pdf
├── README.md
├── copulas.ipynb
├── get_financial_data.ipynb
├── kriging.ipynb
├── time_series_analysis.ipynb
├── figures
│   ├── ...
├── sources
│   ├── ...
└── utils
    └── functions.py
