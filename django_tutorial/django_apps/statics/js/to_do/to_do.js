$(document).ready(function () {
    getAllTasks();
})

const getAllTasks = () => {
    $.ajax({
        url: "task_list_view",
        success: function (response) {
            console.log(response)
            response.data.map(function (item) {
                $('.task-list').append('<li>'+ item.title + '</li>')
            })
        }
    })
}
