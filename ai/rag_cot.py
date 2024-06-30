import google.generativeai as palm
from .retriever import query_vector_database

palm.configure(api_key='AIzaSyCFPXxgS8Stxq975EZSM9Rn71Q5naJXHqs')

def rag_generate_response(prompt):
    model = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods][0].name
    response = palm.generate_text(
        prompt=prompt,
        model=model,
        temperature=0.1,
        max_output_tokens=64,
        top_p=0.9,
        top_k=40,
        stop_sequences=['\n']
    )
    return response.result

def process_query_with_chain_of_thought(user_query, previous_context):
    try:
        initial_response = rag_generate_response(user_query)
        relevant_info = query_vector_database(user_query, previous_context)
        thought_steps = develop_reasoning_steps(initial_response, previous_context, relevant_info)
        final_response = refine_response_based_on_thought_steps(thought_steps)
        return final_response
    except Exception as e:
        raise RuntimeError(f"Error processing query with chain of thought: {str(e)}")

def develop_reasoning_steps(initial_response, previous_context, relevant_info):
    return f"Reasoning based on {initial_response}, {previous_context}, and {relevant_info}"

def refine_response_based_on_thought_steps(thought_steps):
    return f"Refined response: {thought_steps}"
