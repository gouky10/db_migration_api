# FastAPI DB Migration and Metrics API

This project provides a FastAPI-based API for uploading historical data from CSV files to a SQL database, and for retrieving specific metrics about the data.

## Requirements

- Docker
- Docker Compose

## Running the Application

### With Docker Compose
1. Build and run the Docker containers:

```bash
docker-compose up --build
```

2. The API will be available at http://127.0.0.1:8000.

## API Endpoints
### Upload Endpoints
- Upload Departments CSV

```bash
POST /upload_departments/
```
Upload a CSV file with department data.

- Upload Jobs CSV

```bash
POST /upload_jobs/
```
Upload a CSV file with job data.

- Upload Employees CSV

```bash
POST /upload_employees/
```
Upload a CSV file with employee data.

### Metrics Endpoints
- Hires Per Quarter

```bash
GET /metrics/hires_per_quarter/
```
Retrieve the number of employees hired for each job and department in the specified year, divided by quarter.

- Departments Above Mean Hires

```bash
GET /metrics/departments_above_mean/
```
List departments that hired more employees than the mean in the specified year.

## Example CSV Structures
### departments.csv
```
id,name
1,Supply Chain
2,Maintenance
3,Staff
```
### jobs.csv
```
id,title
1,Recruiter
2,Manager
3,Analyst
```
### employees.csv
```
id,name,datetime,department_id,job_id
4535,Marcelo Gonzalez,2021-07-27T16:02:08Z,1,2
4572,Lidia Mendez,2021-07-27T19:04:09Z,1,2
```

## Testing
1. Install test dependencies:

```bash
pip install pytest httpx
```

2. Run tests:

```bash
pytest
```

## Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

