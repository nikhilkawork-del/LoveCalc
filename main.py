import os
import html
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# The specific IP identified from your logs
BANNED_IP = "152.56.253.118"

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("valentine.html", {"request": request, "result": None})

@app.post("/match", response_class=HTMLResponse)
async def calculate_match(request: Request, name1: str = Form(...), name2: str = Form(...)):
    user_ip = request.client.host
    
    # 1. IP Ban: Stop the spammer immediately
    if user_ip == BANNED_IP:
        raise HTTPException(status_code=403, detail="Access Denied")

    # 2. Sanitize and Normalize
    # html.escape prevents the <script> redirects you saw earlier
    safe_n1 = html.escape(name1.strip())
    safe_n2 = html.escape(name2.strip())
    n1_lower = safe_n1.lower()
    n2_lower = safe_n2.lower()
    names_combined = f"{n1_lower} {n2_lower}"

    # 3. Spam Keywords: Avoid writing "HACKED" or "BYPASS" to logs
    spam_keywords = ["hacked", "bypass", "script", "http", "alert"]
    is_spam = any(word in names_combined for word in spam_keywords)

    # 4. Math Logic (Intersection)
    x = list(n1_lower)
    l = list(n2_lower)
    match_count = 0
    for char in l[:]: 
        if char in x:
            match_count += 1
            x.remove(char)
            l.remove(char)
            
    total_possible = min(len(n1_lower), len(n2_lower))
    p = (match_count / total_possible) * 100 if total_possible > 0 else 0

    # 5. Rigged logic
    if "mayuri" in names_combined and "nimit" in names_combined:
        match_percent = 100
    elif "bindu" in names_combined and "krish" in names_combined:
        match_percent = 100
    elif "siyah" in names_combined and "justin bieber" in names_combined:
        match_percent = 100
    elif "shreyashi" in names_combined and "kartik" in names_combined:
        match_percent = 100
    elif "nimit" in names_combined or "nikhil" in names_combined:
        match_percent = 100
    elif "shravani" in names_combined and "anuj" in names_combined:
        match_percent = 100
    else:
        match_percent = min(round(p, 2), 100.0)

    # 6. Secure Logging: Only write if NOT spam
    if not is_spam:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("visitors.txt", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] IP: {user_ip} | Match: {safe_n1} + {safe_n2}\n")

    message = "A perfect pair! 💍" if match_percent > 80 else "Great chemistry! ⚡"

    return templates.TemplateResponse("valentine.html", {
        "request": request,
        "result": {
            "percent": int(match_percent),
            "names": f"{safe_n1} ❤️ {safe_n2}", 
            "message": message
        }
    })

@app.get("/9914173314")
async def view_logs():
    if os.path.exists("visitors.txt"):
        with open("visitors.txt", "r") as f:
            content = f.read()
        return HTMLResponse(content=f"<pre style='padding:20px; background:#1a1a1a; color:#0f0;'>{content}</pre>")
    return "No visitors logged yet."
