document.addEventListener('DOMContentLoaded', () => {
    // 1. Floating Hearts Background
    const createHeart = () => {
        const heart = document.createElement('div');
        heart.innerHTML = '❤️';
        heart.style.cssText = `
            position: fixed;
            bottom: -5vh;
            left: ${Math.random() * 100}vw;
            font-size: ${Math.random() * 20 + 15}px;
            color: rgba(255, 77, 109, ${Math.random() * 0.7 + 0.3});
            user-select: none;
            pointer-events: none;
            z-index: -1;
            transition: transform 6s linear, opacity 6s linear;
        `;
        
        document.body.appendChild(heart);

        requestAnimationFrame(() => {
            heart.style.transform = `translateY(-115vh) rotate(${Math.random() * 720 - 360}deg)`;
            heart.style.opacity = '0';
        });

        setTimeout(() => heart.remove(), 6000);
    };

    setInterval(createHeart, 300);

    // 2. Suspense Animation for the Form
    const loveForm = document.getElementById('loveForm');
    if (loveForm) {
        loveForm.addEventListener('submit', (e) => {
            const btn = loveForm.querySelector('.match-btn');
            btn.innerHTML = "Calculating Vibes... ✨";
            btn.style.pointerEvents = 'none';
            btn.style.opacity = '0.8';
        });
    }

    // 3. High Score Celebration
    // If the percentage element exists and is > 85, trigger a burst
    const percentElement = document.querySelector('.percentage');
    if (percentElement) {
        const score = parseInt(percentElement.innerText);
        if (score > 85) {
            triggerHeartBurst();
        }
    }
});

// Extra effect for soulmates
function triggerHeartBurst() {
    for(let i = 0; i < 20; i++) {
        setTimeout(() => {
            const burstHeart = document.createElement('div');
            burstHeart.innerHTML = '💖';
            burstHeart.style.cssText = `
                position: fixed;
                top: 50%;
                left: 50%;
                font-size: 30px;
                user-select: none;
                pointer-events: none;
                z-index: 100;
                transition: all 1s ease-out;
            `;
            document.body.appendChild(burstHeart);

            const angle = Math.random() * Math.PI * 2;
            const velocity = Math.random() * 200 + 100;
            const tx = Math.cos(angle) * velocity;
            const ty = Math.sin(angle) * velocity;

            requestAnimationFrame(() => {
                burstHeart.style.transform = `translate(${tx}px, ${ty}px) scale(0) rotate(360deg)`;
                burstHeart.style.opacity = '0';
            });

            setTimeout(() => burstHeart.remove(), 1000);
        }, i * 50);
    }
}
document.addEventListener('DOMContentLoaded', () => {
    // Floating background hearts logic...
    // (Keep your existing heart-spawning code here)

    const loveForm = document.getElementById('loveForm');
    if (loveForm) {
        loveForm.addEventListener('submit', (e) => {
            const btn = loveForm.querySelector('.match-btn');
            btn.innerHTML = 'Analyzing Soul Ties...';
            // Optional: You could add a progress bar here
        });
    }
});