
from vllm import LLM, SamplingParams

# Sample Prompts
prompts = [
    "hello, my name is", 
    "The president of the United States is", 
    "The Capital of France is",
    "The Future of AI is",
]

sampling_prams = SamplingParams(temperature=0.8, top_p=0.95)

def main():
    # Create an LLM
    llm = LLM(model="facebook/opt-125m")
    outputs = llm.generate(prompts, sampling_params)

    print("\nGenerated Outputs:\n" + "-" *60)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].generated_text
        print(f"Prompt:     {prompt!r}")
        print(f"Output:     {generated_text!r}")
        print("-" * 60)

if __name == "__main__":
    main()