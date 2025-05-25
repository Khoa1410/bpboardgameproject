document.addEventListener("DOMContentLoaded", () => {
    const randomPlayer = document.getElementById("stgame");

    randomPlayer.addEventListener("click", () => {
        fetch("/Random-Player", {
            method: "POST"
        })
        .then(res => res.json())
        .then(data => {
            // Lưu thông tin vào localStorage
            localStorage.setItem("chosenPlayer", data.namevalue);
            localStorage.setItem("playCount", 1);
            // Chuyển trang
            window.location.href = "/game";
        })
        .catch(error => {
            alert("Lỗi: " + error);
        });
    });
});
