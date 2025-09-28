# Hadoop Inverted Index (with Docker)

This project demonstrates **Big Data processing with Hadoop Streaming** inside a **Dockerized environment**.  
It solves two problems using Python MapReduce:

1. **Inverted Index** → Build an index mapping words to the list of documents in which they appear.  
2. **Top 10 Most Common Words** → Identify the 10 words appearing in the most documents, with tie-breaking handled alphabetically.  

---

## 🐳 Run with Docker

### Pull the image
```bash
docker pull amaanelahi30/hadoop-inverted-index:latest
