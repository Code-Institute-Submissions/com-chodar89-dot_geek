$(function () {
    let selectField = $('#id_product_type');
    let clothingStock = $('.field-stock_xs, .field-stock_s, .field-stock_m, .field-stock_l, .field-stock_xl, .field-stock_xxl, .field-stock_xxxl');
    let stock = $('.field-stock');

    function toggleVerified(value) {
        if (value == 1) {
            clothingStock.show();
            stock.show();
        } else {
            clothingStock.hide();
            stock.show();
        }
    }

    // show/hide on load based on pervious value of selectField
    toggleVerified(selectField.val());

    // show/hide on change
    selectField.change(function () {
        toggleVerified($(this).val());
    });
});
