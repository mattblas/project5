document.addEventListener('DOMContentLoaded', function() {

    // // Use buttons to toggle between views
    document.querySelector('#add_new_route_button').addEventListener('click', () => add_new_route());
    document.querySelector('#edit_route_button').addEventListener('click', () => edit_route());
    document.querySelector('#download_score_button').addEventListener('click', () => download_score());
    document.querySelector('#do_something_button').addEventListener('click', () => do_something());
 
    // // By default, load the inbox
    add_new_route();
  });

function add_new_route() {
    document.querySelector('#add_new_route').style.display = 'block';
    document.querySelector('#edit_route').style.display = 'none';
    document.querySelector('#download_score').style.display = 'none';
    document.querySelector('#do_something').style.display = 'none';
}

function edit_route() {
    document.querySelector('#add_new_route').style.display = 'none';
    document.querySelector('#edit_route').style.display = 'block';
    document.querySelector('#download_score').style.display = 'none';
    document.querySelector('#do_something').style.display = 'none';
}

function download_score() {
    document.querySelector('#add_new_route').style.display = 'none';
    document.querySelector('#edit_route').style.display = 'none';
    document.querySelector('#download_score').style.display = 'block';
    document.querySelector('#do_something').style.display = 'none';
}

function do_something() {
    document.querySelector('#add_new_route').style.display = 'none';
    document.querySelector('#edit_route').style.display = 'none';
    document.querySelector('#download_score').style.display = 'none';
    document.querySelector('#do_something').style.display = 'block';
}

function edit_route_form(id) {
    document.querySelector('#add_new_route').style.display = 'none';
    document.querySelector('#edit_route').style.display = 'none';
    document.querySelector('#download_score').style.display = 'none';
    document.querySelector('#do_something').style.display = 'none';
    document.querySelector('#edit_route_form').style.display = 'block';

    fetch(`/edit_route_form/${id}`)
    .then(response => response.json())
    .then(data => {
        console.log(data);
})}