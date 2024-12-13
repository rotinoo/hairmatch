# HairMatch
HairMatch is a machine learning-powered web application that helps users discover men's hairstyles that best suit their facial features and preferences. The project integrates machine learning, Python, and Jupyter Notebook for processing and analysis, delivering recommendations through an intuitive interface. This 

## Features
Face Type Classification: Uses a machine learning model to classify face types.
Hair Type Classification: Uses a machine learning model to classify hair types.
Hairstyle Recommendations: Matches users with hairstyles based on analysis.
Interactive Interface: Easy-to-use web interface for exploring results.
Model API: Powered by a Flask server to provide model endpoints.

## Dataset that we use
Face type dataset :
[https://storage.googleapis.com/dataset-hairmatch](https://console.cloud.google.com/storage/browser/dataset-hairmatch)
or you could download with
`gsutil -m cp -r gs://dataset-hairmatch`

Hair type dataset :
[https://storage.googleapis.com/hairtype-dataset](https://console.cloud.google.com/storage/browser/hairtype-dataset)
or you could download with
`gsutil -m cp -r gs://hairtype-dataset`


## Getting Started  with GCP
This guide focuses on deploying HairMatch using Google Cloud Platform (GCP).

### Prerequisites
Ensure you have:
- A GCP account and a project set up.
- The Google Cloud SDK (gcloud) installed and configured.

#### Clone directory
```bash
   git clone https://github.com/rotinoo/hairmatch.git
```

### Deployment :
We are deploying backend in cloud run and front end in app enginge

#### Backend :
Make sure you already clone the directory then

1. Navigate to the backend directory :
```bash
cd hairmatch/Web_Application/hairmatch-be
```
2. Build the Docker image:
```bash
docker build -t hairmatch-backend .
```
3. Deploy the Docker container to Cloud Run:
```
gcloud run deploy --image gcr.io/[YOUR_PROJECT_ID]/hairmatch-backend --platform managed
```

Once deployed, note the provided Cloud Run URL.
You can now proceed to configure and access the application through the deployed endpoints.
to learnmore about the api go to README.md in the backend directory

#### Frontend :
1. Navigate to the frontend directory :
```bash
cd hairmatch/Web_Application/hairmatch-fe
```
2. Use any of code editor to edit utils/api_clint.py Change the base_url variable to yours backend url
   ![image](https://github.com/user-attachments/assets/4235a547-4d74-43d3-bcd8-a9765be54d78)
3. Make sure your app engine in the gcp is already setup and then deploy it
```
gcloud app deploy
```
Once deployed, you can access the application through the provided App Engine URL.
