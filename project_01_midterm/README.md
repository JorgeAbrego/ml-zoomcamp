# Smoker Status Prediction using Bio-Signals

## Table of Contents
1. [Introduction](#introduction)
2. [Datasets](#datasets)
3. [Prerequisites](#prerequisites)
4. [Installation Steps](#installation-steps)
5. [Deployment](#deployment)
6. [Usage](#usage)

## Introduction
Smoking has been proven to negatively affect health in a multitude of ways. It harms nearly every organ of the body, causes many diseases, and reduces the life expectancy of smokers. As of 2018, smoking is the leading cause of preventable morbidity and mortality worldwide.

A report by the World Health Organization predicts that the number of deaths caused by smoking will reach 10 million by 2030.

Despite the promotion of evidence-based treatments for smoking cessation, less than one-third of participants achieve the goal of abstinence. Counseling for smoking cessation is often seen as ineffective and time-consuming by many physicians, who do not routinely practice it. To address this, various factors have been proposed to identify smokers with a better chance of quitting. However, the individual use of these factors for prediction can lead to conflicting and non-straightforward results for both physicians and patients. Predictive models using machine learning have emerged as a favorable solution to understand the chance of quitting smoking for each individual smoker.

A group of scientists are working on predictive models with smoking status as the prediction target. The task is to assist in creating a machine learning model to identify an individual's smoking status using bio-signals.

The goal is to use the provided bio-signal data to predict the smoking status of individuals, aiding in the broader effort to support smoking cessation initiatives and improve global health.

## Dataset
This project is based on a dataset found on Kaggle:

https://www.kaggle.com/datasets/gauravduttakiit/smoker-status-prediction-using-biosignals/data

TThe dataset contains the following columns:

- `age`: Age categorized in 5-year gaps.
- `height(cm)`: Height of the individual in centimeters.
- `weight(kg)`: Weight of the individual in kilograms.
- `waist(cm)`: Waist circumference length in centimeters.
- `eyesight(left)`: Left eye vision measurement.
- `eyesight(right)`: Right eye vision measurement.
- `hearing(left)`: Left ear hearing measurement.
- `hearing(right)`: Right ear hearing measurement.
- `systolic`: Systolic blood pressure measurement.
- `relaxation`: Blood pressure measurement during relaxation.
- `fasting blood sugar`: Measurement of blood sugar levels after fasting.
- `Cholesterol`: Total cholesterol measurement.
- `triglyceride`: Triglyceride level measurement.
- `HDL`: High-Density Lipoprotein (cholesterol type) level measurement.
- `LDL`: Low-Density Lipoprotein (cholesterol type) level measurement.
- `hemoglobin`: Hemoglobin level measurement.
- `Urine protein`: Measurement of protein in urine.
- `serum creatinine`: Serum creatinine level measurement.
- `AST`: Measurement of glutamic oxaloacetic transaminase type.
- `ALT`: Measurement of glutamic oxaloacetic transaminase type.
- `Gtp`: γ-GTP measurement.
- `dental caries`: Dental caries status.
- `smoking`: Smoking status of the individual.

## Prerequisites:

- `git`: For cloning the repository.
- `anaconda` or `conda`: For creating and managing the virtual environment.
- `docker`: For local deployment

## Installation Steps:

### Conda Environment

1. **Clone the Repository**:
   
   Start by cloning the `ml-zoomcamp` repository from GitHub into a directory of your choice (`<folder_name>`). Replace `<folder_name>` with the desired directory name:

   ```bash
   git clone https://github.com/JorgeAbrego/ml-zoomcamp.git <folder_name>
   ```

2. **Navigate to the Project Directory**:

    Once the repository is cloned, navigate to the `project_01_midterm` directory inside it:

   ```bash
   cd <folder_name>/project_01_midterm
   ```

3. **Create a Conda Virtual Environment**:

    Next, set up a new conda virtual environment named `ml-midterm` using Python 3.10:

   ```bash
   conda create -n ml-midterm python=3.10
   ```

4. **Activate the Virtual Environment**:

    With the environment created, activate it using:

   ```bash
   conda activate ml-midterm
   ```

5. **Install Required Dependencies**:

    The project has a list of required libraries and packages specified in the `requirements.txt` file. Install these using:

   ```bash
   pip install -r requirements.txt
   ```

### Pipenv Environment

1. **Install pipenv**:

   Install Pipenv by running the following command:

   ```bash
   pip install pipenv
   ```
2. **Create a Virtual Environment**:

   Create a virtual environment using Pipenv.

   ```bash
   pipenv --python 3.10
   ```

3. **Install Dependencies from Pipfile.lock**:

   Install all the dependencies specified in the Pipfile.lock by running the following command:

   ```bash
   pipenv sync
   ```

4. **Activate the Virtual Environment**:
   
   Activate the Virtual Environment

   ```bash
   pipenv shell
   ```

To exit the virtual environment and return to your global Python environment, simply type `exit` and press `Enter`.

## Deployment

### Local Run

**Running the Service on Linux Using Gunicorn**

To run the service locally on a Linux system utilizing the Gunicorn WSGI HTTP Server, follow these steps:

```bash
pipenv run gunicorn --bind 0.0.0.0:9696 predict:app
```

This command starts Gunicorn and binds it to all network interfaces on port `9696`, allowing the `predict:app` to be accessible. To stop the service, press `Ctrl+C` in the terminal.

**Running the Service on Windows Using Waitress**

For running the service on a Windows platform, the Waitress server is employed. Execute the following command:

```bash
pipenv run waitress-serve --listen=0.0.0.0:9696 predict:app
```

This instruction initiates the Waitress server, listening on all network interfaces at port `9696`, serving the `predict:app`. To stop the service, press `Ctrl+C`in the command prompt.

**Note**: Ensure that the environment and dependencies are correctly set up and the required libraries are installed for a seamless execution of the service.

### Docker Container

Execute the following command to build the Docker image. This will create an image with the tag `smoking-predictor:v1` (you can pick another name if you want).

```bash
docker build -t smoking-predictor:v1 .
```

This process might take several minutes as Docker needs to download the base images and build the necessary layers for your application.

Run the following command to start a container based on the image you just created. This command also maps port `9696` of the container to port `9696` on your local machine.

```bash
docker run -it --name SmokingPredictor -p 9696:9696 smoking-predictor:v1
```

Upon executing this command, the container will start, and you should be able to interact with the prediction model through the specified port.

To stop the service, press `Ctrl+C` in the command prompt.

### AWS Elastic Beanstalk

TODO

## Usage

TODO