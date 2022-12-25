//This code allows the user to toggle the comment by clicking on it
const comments = document.querySelectorAll('.comments');
comments.forEach((comment) => {
    comment.addEventListener('click', (event) => {
        const commentField = event.currentTarget.querySelector('.comment-field');
        commentField.style.display = commentField.style.display === 'none' ? 'block' : 'none';
    });
});

//display alerts
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000);