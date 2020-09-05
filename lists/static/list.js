window.Superlists = {};
window.Superlists.initialize = function () {
    console.log("注册监听器")
    $('input[name="text"]').on('keypress', function () {
        $('.has-error').hide();
    });
};