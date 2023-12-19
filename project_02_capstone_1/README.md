# Vegetable Classification Using Deep Convolutional Neural Networks

![Dataset Cover](images/dataset-cover.png)

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Prerequisites](#prerequisites)
4. [Installation Steps](#installation-steps)
5. [Deployment](#deployment)
6. [Usage](#usage)

## Introduction

In the realm of agricultural technology and food industry, the accurate classification of vegetables plays a crucial role in various processes from quality control in production lines to inventory management in retail environments. This project aims to harness the power of Deep Learning, particularly Convolutional Neural Networks (ConvNets), to develop an advanced system capable of recognizing and classifying 15 different vegetable classes with high accuracy.

### Background

The traditional methods of vegetable classification often involve manual inspection and basic image processing techniques, which can be time-consuming, error-prone, and inefficient. With the advent of Deep Learning, and specifically ConvNets, there has been a significant shift in how image classification tasks are approached. ConvNets, known for their ability to detect and extract features from images, have revolutionized the field of computer vision, leading to breakthroughs in various applications, including facial recognition, medical imaging, and now, in the agricultural sector.

### Project Objective

The primary goal of this project is to develop a ConvNet-based model that can accurately recognize and classify 15 different types of vegetables. This model will be trained on a diverse dataset comprising thousands of labeled images of vegetables. The dataset will include various images for each vegetable type, capturing different angles, lighting conditions, and backgrounds to ensure the model is robust and generalizable.

### Potential Applications

The successful development of this ConvNet model opens up numerous practical applications:

* Quality Control in Agriculture: Automated sorting and grading of vegetables based on quality, size, and type, enhancing efficiency in packaging and distribution.
* Retail Management: Integration with inventory systems in supermarkets for automatic stock updates, reducing manual labor and improving inventory accuracy.
* Educational Tools: Serving as a learning aid in educational settings for students studying botany, nutrition, or agriculture.

## Dataset

The dataset is a comprehensive collection designed for an experiment involving the classification of common vegetables. It includes 15 types of widely-found vegetables: bean, bitter gourd, bottle gourd, brinjal, broccoli, cabbage, capsicum, carrot, cauliflower, cucumber, papaya, potato, pumpkin, radish, and tomato. A total of 21,000 images, distributed evenly across these 15 classes, have been used. Each class contributes 1,400 images, all standardized to a size of 224×224 pixels and saved in the *.jpg format.

The dataset is split into three distinct sets for training, validation, and testing:

* Training Set: 70% of the total dataset, amounting to 15,000 images.
* Validation Set: 15% of the dataset, comprising 3,000 images.
* Testing Set: The remaining 15%, also including 3,000 images.

Each set is organized into subfolders categorized by vegetable type, ensuring easy access and management of the images.

The full dataset is available at [Kaggle](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset/). For convenience, we have also provided a compressed version of the dataset in this repository, into data folder.

## Prerequisites:

- `git`: For cloning the repository.
- `anaconda` or `conda`: For creating and managing the virtual environment.
- `docker`: For local deployment and testing.
- `AWS CLI`: To work with AWS.
- `Insomnia`: For API testing.

## Installation Steps:

### Conda Environment for Experimentation

1. **Clone the Repository**:
   
   Start by cloning the `ml-zoomcamp` repository from GitHub into a directory of your choice (`<folder_name>`). Replace `<folder_name>` with the desired directory name:

   ```bash
   $ git clone https://github.com/JorgeAbrego/ml-zoomcamp.git <folder_name>
   ```

2. **Navigate to the Project Directory**:

    Once the repository is cloned, navigate to the `project_02_capstone_1` directory inside it:

   ```bash
   $ cd <folder_name>/project_01_midterm
   ```

3. **Create a Conda Virtual Environment**:

    Next, set up a new conda virtual environment named `ml-project-1` using Python 3.10:

   ```bash
   $ conda create -n ml-project-1 python=3.10
   ```

4. **Activate the Virtual Environment**:

    With the environment created, activate it using:

   ```bash
   $ conda activate ml-project-1
   ```

5. **GPU setup**:
    Before installing modules to be used in this project, you have to install required libraries for GPU. You can skip this section if you only run TensorFlow on CPU. More information [here](https://www.tensorflow.org/install/pip).

    ```bash
    $ conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
    ```

6. **Install Required Dependencies**:

    The project has a list of required libraries and packages specified in the `requirements.txt` file. Install these using:

   ```bash
   $ pip install -r requirements.txt
   ```

## Deployment

### Local Test (Docker Container)

Execute the following command to build the Docker image. This will create an image with the tag `vegetables-classifier:v1` (you can pick another name if you want).

```bash
$ docker build -t vegetable-classifier:v1 .
```

This process might take several minutes as Docker needs to download the base images and build the necessary layers for your application.

Run the following command to start a container based on the image you just created. This command also maps port `8080` of the container to port `8080` on your local machine.

```bash
$ docker run -it --name Vegetable-Classifer -p 8080:8080 vegetable-classifier:v1
```

### Pulling image to AWS ECR


### AWS Lambda


### AWS API Gateway



## Usage

### Using Test Python Files

For testing this API using the provided Python scripts: test-cloud.py for cloud-based tests and test-local.py for local tests.

*Local Test*

To test the API locally, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory containing the test-local.py script.
3. Execute the script by running:

   ```bash
   python test_local.py
   ```

Example:

![Local Test](images/file_test_local.png)

*Cloud Test*

For testing the cloud-based API, the steps are similar:

1. Open your terminal or command prompt.
2. Navigate to the directory containing the test-cloud.py script.
3. Execute the script by running:

   ```bash
   python test-cloud.py
   ```

Example:

![Local Test](images/file_test_cloud.png)

### Using API Client

There are several clients available for testing API applications, and one of the notable ones is `Insomnia`. It's a powerful and flexible tool designed for interacting with APIs. It enables developers to set up, send, and analyze HTTP requests and responses with ease. If you don't have Insomnia on your machine, it's easy to get started by downloading it from [here](https://insomnia.rest/download).

**Step 1: Navigating the Initial Menu of Insomnia**

Upon opening Insomnia for the first time, you'll be presented with the initial menu where you can either create a new request or open an existing workspace. To get started, click on `New HTTP Request`

![Insomnia Main](images/insomnia_main.png)

**Step 2: Configuring the Request**

1. **URL**: Enter the address of the API endpoint you wish to communicate with in the URL bar

2. **Method**: Choose the appropriate method for your request (for example, POST) from the dropdown menu next to the URL bar.

3. **JSON Data**: If you are executing a method such as POST or PUT that requires a message body, select 'Body' beneath the URL bar. Then choose 'JSON' and enter or paste the JSON you wish to send in the request body.

4. **Send request**: Clic on `Send` button to make the request to server.

![Insomnia Configuration](images/insomnia_config.png)

**Step 3: Example of Response**

After you have configured your request and sent it, Insomnia will display the response in the same window.

These are examples in local and cloud deployment:

*Local Test*

For local testing, just fill the local address in URL box

![Local Test](images/insomnia_test_local.png)

*Cloud/Remote Test*

For cloud/remote testing, just fill API remote address in URL box

![Cloud Test](images/insomnia_test_cloud.png)