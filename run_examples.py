# scripts/run_examples.py
import os
import sys
import json

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.main import main

def run_example(name, task, context=""):
    """Run an example task and save the results."""
    print(f"Running example: {name}")
    print(f"Task: {task}")
    print("-" * 50)
    
    result = main(task, context)
    
    # Save result to file
    os.makedirs("data/output", exist_ok=True)
    output_file = f"data/output/example_{name.lower().replace(' ', '_')}.json"
    
    with open(output_file, "w") as f:
        json.dump(result, f, indent=2)
    
    print(f"Results saved to {output_file}")
    print("=" * 50)
    
    return result

if __name__ == "__main__":
    examples = [
        {
            "name": "Research Task",
            "task": "Research the benefits of microservices architecture",
            "context": ""
        },
        {
            "name": "Summarization Task",
            "task": "Summarize the key points from the provided text",
            "context": "Microservices architecture is an approach to software development where applications are built as a collection of small, independent services. Each service runs in its own process and communicates with other services through well-defined APIs. This approach allows for better scalability, faster development cycles, and improved fault isolation compared to monolithic architectures."
        }
    ]
    
    for example in examples:
        run_example(**example)

