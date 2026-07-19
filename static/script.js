function setupShowstopperCar() {
    const car = document.querySelector(".solar-car");

    if (!car) {
        setTimeout(setupShowstopperCar, 300);
        return;
    }

    document.body.appendChild(car);
    car.classList.add("showstopper-car");

    let targetProgress = 0;
    let smoothProgress = 0;

    function updateTarget() {
        const maxScroll =
            document.documentElement.scrollHeight - window.innerHeight;

        targetProgress =
            maxScroll > 0 ? window.scrollY / maxScroll : 0;
    }

    function animateCar() {
        smoothProgress +=
            (targetProgress - smoothProgress) * 0.06;

        const screenHeight = window.innerHeight;

        // Vertical movement between safe top and bottom areas
        const minY = 130;
        const maxY = screenHeight - 260;
        const y =
            minY + smoothProgress * (maxY - minY);

        // Smooth curved zig-zag movement
        const curve =
            Math.sin(smoothProgress * Math.PI * 6) * 55;

        // Slight tilt while turning
        const tilt =
            Math.cos(smoothProgress * Math.PI * 6) * 5;

        car.style.transform =
            `translate(${curve}px, ${y}px) rotate(${tilt}deg)`;

        requestAnimationFrame(animateCar);
    }

    window.addEventListener("scroll", updateTarget);
    window.addEventListener("resize", updateTarget);

    updateTarget();
    animateCar();
}

window.addEventListener("load", setupShowstopperCar);