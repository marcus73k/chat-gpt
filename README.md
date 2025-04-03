# GPT Analyzer

A command-line tool for analyzing data using OpenAI's GPT models. This tool can process input from various sources and provide AI-powered analysis.

## Features

- Analyze data from stdin, stderr files, or command-line parameters
- Docker support for easy deployment
- Automatic Docker image building via GitHub Actions

## Installation

### Prerequisites

- Python 3.x
- OpenAI API key

### Direct Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chat-gpt.git
   cd chat-gpt
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Docker Installation

Pull the pre-built image:
```bash
docker pull ghcr.io/your-username/gpt-analyzer:latest
```

Or build locally:
```bash
docker build -t gpt-analyzer .
```

## Usage

### Basic Usage

```bash
# Using direct installation
./gpt.py --api-key YOUR_API_KEY "text to analyze"

# Using stdin
echo "analyze this text" | ./gpt.py --api-key YOUR_API_KEY

# Using Docker
docker run --rm -e OPENAI_API_KEY=YOUR_API_KEY ghcr.io/your-username/gpt-analyzer "text to analyze"
```

### Analyzing Error Output

```bash
# Save error output to a file
your-command 2> error.txt

# Analyze the error
./gpt.py --api-key YOUR_API_KEY --error-file error.txt
```

### Environment Variables

You can set the OpenAI API key as an environment variable instead of using the command-line argument:

```bash
export OPENAI_API_KEY=your-api-key
./gpt.py "text to analyze"
```

## CI/CD

This repository includes GitHub Actions workflows for:

- Automatically building and pushing Docker images to GitHub Container Registry on commits to the master branch
- Supporting multiple platforms (linux/amd64, linux/arm64)

## License

[Your license information here]
