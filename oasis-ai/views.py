from django.contrib.messages.context_processors import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import StreamingHttpResponse
import ollama


# Create your views here.

@login_required
def index(request):
    return redirect("oasis-chat:ollama_chat")

@login_required
def chat(request):
    return render(request, "oasis-ai/chat.html")

@csrf_exempt
def ollama_chat(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt", "")
        print(prompt)
        def stream():
            for response in ollama.chat(model="deepseek-r1:1.5b",
                                        messages=[{"role": "user",
                                                   "content": prompt}],
                                        stream=True):
                yield response["message"]["content"]

        return StreamingHttpResponse(stream(), content_type="text/plain")

    return render(request, "oasis-ai/chat.html")

@csrf_exempt
def ollama_translate(request):
    if request.method == "POST":
        text = request.POST.get("text", "")
        language = request.POST.get("language", "")
        content = "translate: '" + text + "' to: " + language
        messages = [{"role": "user", "content": content}]
        print(messages)
        def stream():
            for response in ollama.chat(model="lauchacarro/qwen2.5-translator",
                                        messages=messages,
                                        stream=True):
                yield response["message"]["content"]

        return StreamingHttpResponse(stream(), content_type="text/plain")

    return render(request, "oasis-ai/chat.html")