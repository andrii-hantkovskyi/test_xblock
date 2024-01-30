/* Javascript for TestXBlock. */
function TestXBlock(runtime, element) {

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) {
            return parts.pop().split(';').shift();
        }
    }

    var handlerAddUrl = runtime.handlerUrl(element, 'add_topic');
    var handlerPopUrl = runtime.handlerUrl(element, 'pop_topic');


    $(function ($) {
        $('.testxblock_block', element).attr('hx-headers', `"X-CSRFToken": "${getCookie('csrftoken')}"`)
        $('.questions_new__form', element).attr('hx-post', handlerAddUrl)
        $('#pop_question', element).attr('hx-post', handlerPopUrl)
        $('.suggestions_new__form', element).attr('hx-post', handlerAddUrl)
        $('#pop_suggestion', element).attr('hx-post', handlerPopUrl)
    });
}
