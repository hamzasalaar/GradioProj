import gradio as gr

def selection_sort(arr):
    arr = arr.copy()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def sort_array(input_array, algorithm):
    arr = [int(x) for x in input_array.split(',')]
    if algorithm == "Selection Sort":
        sorted_arr = selection_sort(arr)
    elif algorithm == "Insertion Sort":
        sorted_arr = insertion_sort(arr)
    return str(sorted_arr)

input_array = gr.Textbox(lines=1, placeholder="Enter array elements separated by commas (e.g., 4,1,0,3,2)")
algorithm = gr.Dropdown(choices=["Selection Sort", "Insertion Sort"], label="Sorting Algorithm")
output = gr.Textbox()

output = gr.Interface(fn=sort_array, inputs=[input_array, algorithm], outputs=output, 
             title="Analysis of Algorithms Mini Project",
             description="Simple user interface to show a sorting algorithm",
             theme="dark")
output.launch()
