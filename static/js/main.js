/* =============================
   DAILY AFFIRMATION GENERATOR
============================= */

document.addEventListener('DOMContentLoaded', () => {
    const affirmBox = document.getElementById("affirmBox");
    const affirmText = document.getElementById("affirmText");
    const affirmBtn = document.getElementById("newAffirmBtn");

    if (!affirmBox) return; // kalau elemen tidak ada, aman tidak error

    const affirmations = [
        "Kamu cukup, persis seperti dirimu hari ini.",
        "Satu langkah kecil tetap sebuah progres.",
        "Kamu layak mendapatkan istirahat dan ketenangan.",
        "Tidak apa-apa untuk tidak baik-baik saja, yang penting kamu terus mencoba.",
        "Kamu lebih kuat daripada yang kamu kira.",
        "Kamu pantas untuk bahagia.",
        "Hari ini adalah kesempatan baru untuk berkembang."
    ];

    function generateAffirmation() {
        const random = Math.floor(Math.random() * affirmations.length);
        affirmText.textContent = affirmations[random];
    }

    // generate pertama kali
    generateAffirmation();

    // tombol generate ulang
    affirmBtn.addEventListener("click", generateAffirmation);
});
