import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("valentine.html", {"request": request, "result": None})

@app.post("/match", response_class=HTMLResponse)
async def calculate_match(request: Request, name1: str = Form(...), name2: str = Form(...)):
    # 1. Logging Logic (to see who is using the site)
    user_ip = request.client.host
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 2. Logic: Finding common letters (Intersection)
    x = list(name1.lower().strip())
    l = list(name2.lower().strip())
    match_count = 0
    
    for char in l[:]: 
        if char in x:
            match_count += 1
            x.remove(char)
            l.remove(char)
            
    # Calculate percentage based on the shorter name to keep scores high/fun
    total_possible = min(len(name1.strip()), len(name2.strip()))
    if total_possible > 0:
        p = (match_count / total_possible) * 100
    else:
        p = 0

    # Rigged match for the developer ;)
    names_combined = f"{name1.lower()} {name2.lower()}"
    if "mayuri" in names_combined and "nimit" in names_combined:
        match_percent = 100
    else:
        match_percent = min(round(p, 2), 100.0)

    message = "A perfect pair! 💍" if match_percent > 80 else "Great chemistry! ⚡"
    # In your @app.post("/match") route
    return templates.TemplateResponse("valentine.html", {
        "request": request,
        "result": {
            "percent": match_percent,
            "names": f"{name1.strip()} ❤️ {name2.strip()}", 
            "message": message
        }
    })

    with open("visitors.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] IP: {user_ip} | Match: {name1} + {name2}\n | Percentage : {int(p)} ")

# Secret route to view your logs live on Render
@app.get("/9914173314")
async def view_logs():
    if os.path.exists("visitors.txt"):
        with open("visitors.txt", "r") as f:
            content = f.read()
        return HTMLResponse(content=f"<pre style='padding:20px; background:#1a1a1a; color:#0f0;'>{content}</pre>")
    return "No visitors logged yet."
