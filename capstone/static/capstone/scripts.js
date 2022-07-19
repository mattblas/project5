document.addEventListener('DOMContentLoaded', function() {

    // Use buttons to toggle between views
    document.querySelector('#add_new_route_button').addEventListener('click', () => add_new_route());
    document.querySelector('#edit_route_button').addEventListener('click', () => edit_route());
    document.querySelector('#download_score_button').addEventListener('click', () => download_score());
    document.querySelector('#do_something_button').addEventListener('click', () => do_something());
 
    // By default, load the inbox
    add_new_route();
  });

function add_new_route() {
    document.querySelector('#add_new_route').style.display = 'block';
    document.querySelector('#edit_route').style.display = 'none';
    document.querySelector('#download_score').style.display = 'none';
    document.querySelector('#do_something').style.display = 'none';

    document.querySelector('#add_new_route').innerHTML = `<h4 align="right">Add new route</h4>`;

}

function edit_route() {
    document.querySelector('#add_new_route').style.display = 'none';
    document.querySelector('#edit_route').style.display = 'block';
    document.querySelector('#download_score').style.display = 'none';
    document.querySelector('#do_something').style.display = 'none';

    document.querySelector('#edit_route').innerHTML = `<h4 align="right">Edit route</h4>`;
}

function download_score() {
    document.querySelector('#add_new_route').style.display = 'none';
    document.querySelector('#edit_route').style.display = 'none';
    document.querySelector('#download_score').style.display = 'block';
    document.querySelector('#do_something').style.display = 'none';

    document.querySelector('#download_score').innerHTML = `<h4 align="right">Download score</h4>`;
}

function do_something() {
    document.querySelector('#add_new_route').style.display = 'none';
    document.querySelector('#edit_route').style.display = 'none';
    document.querySelector('#download_score').style.display = 'none';
    document.querySelector('#do_something').style.display = 'block';

    document.querySelector('#do_something').innerHTML = `<h4 align="right">Do something</h4>`;
}