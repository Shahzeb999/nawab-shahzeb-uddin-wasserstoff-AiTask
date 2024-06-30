# System Design

## Overview
This document outlines the design of the RAG-based Query Suggestion Chatbot with Chain of Thought (CoT) for WordPress Sites.

## Components
- **Data Retrieval:** Fetches content updates from WordPress.
- **Embedding Generator:** Converts text to vector embeddings.
- **Vector Database:** Stores and retrieves embeddings.
- **RAG Processor:** Generates initial responses.
- **Chain of Thought Module:** Enhances responses with logical progression.
- **User Interface:** Provides an interactive chat interface.

## Architecture
- **Backend:** Flask server handling API requests and integrating RAG and CoT.
- **Frontend:** WordPress plugin for easy integration and interaction.
- **Vector Database:** Faiss for efficient embedding storage and retrieval.
