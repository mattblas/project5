document.addEventListener('DOMContentLoaded', function() {

    // // Use buttons to toggle between views
    document.querySelector('#cat_open_button').addEventListener('click', () => cat_open());
    document.querySelector('#cat_j_m_button').addEventListener('click', () => cat_j_m());
    document.querySelector('#cat_j_w_button').addEventListener('click', () => cat_j_w());
    document.querySelector('#cat_s_m_button').addEventListener('click', () => cat_s_m());
    document.querySelector('#cat_s_w_button').addEventListener('click', () => cat_s_w());
    document.querySelector('#cat_all_time_button').addEventListener('click', () => cat_all_time());

    // // By default, load the inbox
    cat_open();
  });

  function cat_open() {
    document.querySelector('#cat_open').style.display = 'block';
    document.querySelector('#cat_j_m').style.display = 'none';
    document.querySelector('#cat_j_w').style.display = 'none';
    document.querySelector('#cat_s_m').style.display = 'none';
    document.querySelector('#cat_s_w').style.display = 'none';
    document.querySelector('#cat_all_time').style.display = 'none';
}

function cat_j_m() {
    document.querySelector('#cat_open').style.display = 'none';
    document.querySelector('#cat_j_m').style.display = 'block';
    document.querySelector('#cat_j_w').style.display = 'none';
    document.querySelector('#cat_s_m').style.display = 'none';
    document.querySelector('#cat_s_w').style.display = 'none';
    document.querySelector('#cat_all_time').style.display = 'none';
}

function cat_j_w() {
    document.querySelector('#cat_open').style.display = 'none';
    document.querySelector('#cat_j_m').style.display = 'none';
    document.querySelector('#cat_j_w').style.display = 'block';
    document.querySelector('#cat_s_m').style.display = 'none';
    document.querySelector('#cat_s_w').style.display = 'none';
    document.querySelector('#cat_all_time').style.display = 'none';
}

function cat_s_m() {
    document.querySelector('#cat_open').style.display = 'none';
    document.querySelector('#cat_j_m').style.display = 'none';
    document.querySelector('#cat_j_w').style.display = 'none';
    document.querySelector('#cat_s_m').style.display = 'block';
    document.querySelector('#cat_s_w').style.display = 'none';
    document.querySelector('#cat_all_time').style.display = 'none';
}

function cat_s_w() {
    document.querySelector('#cat_open').style.display = 'none';
    document.querySelector('#cat_j_m').style.display = 'none';
    document.querySelector('#cat_j_w').style.display = 'none';
    document.querySelector('#cat_s_m').style.display = 'none';
    document.querySelector('#cat_s_w').style.display = 'block';
    document.querySelector('#cat_all_time').style.display = 'none';
}

function cat_all_time() {
    document.querySelector('#cat_open').style.display = 'none';
    document.querySelector('#cat_j_m').style.display = 'none';
    document.querySelector('#cat_j_w').style.display = 'none';
    document.querySelector('#cat_s_m').style.display = 'none';
    document.querySelector('#cat_s_w').style.display = 'none';
    document.querySelector('#cat_all_time').style.display = 'block';
}