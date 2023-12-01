 function openModal() {
        document.getElementById('deleteModal').style.display = 'block';
        document.getElementById('modalOverlay').style.display = 'block';
    }

    function closeModal() {
        document.getElementById('deleteModal').style.display = 'none';
        document.getElementById('modalOverlay').style.display = 'none';
    }

    function deleteCategory() {
        // Здесь добавляю логику для удаления выбранной категории
        var selectedCategoryId = document.getElementById('categorySelect').value;
        // Отправить запрос на удаление категории по выбранному ID
        // ...
        // Закрыть модальное окно
        closeModal();
    }


$(document).ready(function () {
   $('.content-container').addClass('show');
});


function setSelectedCategoryId() {
   // Получаем выбранное значение из списка и устанавливаем его в скрытое поле
    var selectedCategoryId = document.getElementById('categorySelect').value;
    document.getElementById('selectedCategoryId').value = selectedCategoryId;
}