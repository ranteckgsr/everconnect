# Everest Forms API (FastAPI + Docker)

This project provides a simple FastAPI-based web API to fetch and display Everest Forms entries from a remote WordPress site. It is fully containerized with Docker for easy sharing and deployment.

## Features
- Fetches entries from a remote Everest Forms REST API
- Returns only the First Name, Phone Number, and File Upload fields for each entry
- Easy to run locally or deploy anywhere with Docker
- Interactive OpenAPI docs at `/docs`

## Requirements
- [Docker](https://www.docker.com/products/docker-desktop/) (Desktop or Engine)

## Quick Start

1. **Clone or download this repository**

2. **Open a terminal in the project directory**

3. **Build the Docker image:**
   ```bash
   docker build -t my-fastapi-app .
   ```

4. **Run the Docker container:**
   ```bash
   docker run -d -p 8000:8000 my-fastapi-app
   ```

5. **Access the API:**
   - API endpoint: [http://localhost:8000/entries?form_id=23031](http://localhost:8000/entries?form_id=23031)
   - Interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## API Usage

### `GET /entries`
**Query Parameters:**
- `form_id` (required): The Everest Forms form ID to fetch entries for
- `status` (optional, default: `publish`): Filter by entry status

**Example:**
```
GET /entries?form_id=23031
```

**Response:**
```json
{
  "entries": [
    {
      "First Name": "John",
      "Phone Number": "1234567890",
      "File Upload": "https://.../file.txt"
    },
    ...
  ]
}
```

## Notes
- You can change the API credentials or WordPress site URL in `main.py` as needed.
- To stop the container: `docker ps` to find the container ID, then `docker stop <container_id>`

---

## WordPress Plugin: custom-evf-global-entries.php

The file `custom-evf-global-entries.php` is a custom WordPress plugin that exposes Everest Forms entries via a REST API. 

**How to install the plugin:**
1. Download or copy `custom-evf-global-entries.php` to your computer.
2. Zip the file if needed (right-click > Send to > Compressed (zipped) folder).
3. Log in to your WordPress admin dashboard.
4. Go to **Plugins > Add New > Upload Plugin**.
5. Upload the PHP file (or zip), then activate the plugin.

This will enable the custom REST API endpoint on your WordPress site.

## Sample File: whatsapp_natural_chat.txt

The file `whatsapp_natural_chat.txt` is provided as a sample file for testing file upload and retrieval features in Everest Forms entries.

---

If you have any issues or questions, feel free to ask!
