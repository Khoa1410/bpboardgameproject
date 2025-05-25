function stdgame(){
    document.addEventListener("DOMContentLoaded", () => {
        const randomPlayer = document.getElementById("stgame");
        const result = document.getElementById("namevalue");

        btn.addEventListener("click", () => {
            result.textContent = "Đang chọn số...";

            fetch("/Random-Player", {
                method: "POST"
            })
            .then(res => res.json())
            .then(data => {
                result.textContent = data.result;
            })
            .catch(error => {
                result.textContent = "Lỗi: " + error;
            });
        });
    });
}