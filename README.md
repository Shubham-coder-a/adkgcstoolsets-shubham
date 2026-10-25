# Google ADK Agent with Google Cloud Storage (GCS)

An AI-powered document assistant built using Google Agent Development Kit (ADK) and Google Cloud Storage. It retrieves information from PDF documents and answers questions with source-file citations.

## 🚀 Project Overview

This project demonstrates how an ADK agent can access documents in a Google Cloud Storage bucket and provide document-grounded answers.

## ✨ Key Features

- Gemini 2.5 Flash-powered AI agent
- Google Cloud Storage integration
- PDF document search and retrieval
- `before_tool_callback` for bucket-target control
- Answers grounded in document content
- Source-file citation in responses
- Testing through the ADK Web interface

## 🏗️ Architecture

User Query → ADK Agent → Security Callback → GCS Toolset → GCS Bucket → PDF Content → Grounded Answer with Source Citation

## 🛠️ Technologies Used

- Python
- Google Agent Development Kit (ADK)
- Gemini 2.5 Flash
- Google Cloud Storage (GCS)
- Google Cloud Shell
- Git and GitHub

## 📸 Project Demonstration

The project was tested using a company travel policy PDF. The agent summarized the policy, listed available bucket files, and identified the source filename.

## 🔐 Security

A `before_tool_callback` is used to control the target bucket. Google Cloud IAM permissions should also be configured appropriately.

## 🙏 Acknowledgements

Special thanks to **Ankush Kathar** and **Ashutosh S. Bhakare** for their guidance and for sharing the project architecture.

## 👨‍💻 Author

**Shubham Nagpure**

GitHub: [Shubham-coder-a](https://github.com/Shubham-coder-a)
