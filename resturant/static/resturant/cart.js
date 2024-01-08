console.log("hello");

document.addEventListener('DOMContentLoaded', function () {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    const updateCartButtons = document.querySelectorAll('.update-cart');
    const removeFromCartButtons = document.querySelectorAll('.remove-from-cart');
    const quantityInputs = document.querySelectorAll('.quantity-input');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function () {
            const itemId = button.dataset.itemId;
            addToCart(itemId);
        });
    });

    updateCartButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();  // Prevent the form from submitting
            const itemId = button.dataset.itemId;
            const quantity = document.querySelector(`.quantity-input[data-item-id="${itemId}"]`).value;
            updateCart(itemId, quantity);
        });
    });

    removeFromCartButtons.forEach(button => {
        button.addEventListener('click', function () {
            const itemId = button.dataset.itemId;
            removeFromCart(itemId);
        });
    });

    function addToCart(itemId) {
        let cart = JSON.parse(localStorage.getItem('cart')) || {};
        cart[itemId] = (cart[itemId] || 0) + 1;
        localStorage.setItem('cart', JSON.stringify(cart));
        console.log("Added to cart")
    }

    function updateCart(itemId, quantity) {
        console.log("updated")
        let cart = JSON.parse(localStorage.getItem('cart')) || {};
        cart[itemId] = parseInt(quantity);
        localStorage.setItem('cart', JSON.stringify(cart));
        alert('Cart updated!');
        location.reload(); 
    }

    function removeFromCart(itemId) {
        let cart = JSON.parse(localStorage.getItem('cart')) || {};
        delete cart[itemId];
        localStorage.setItem('cart', JSON.stringify(cart));
        alert('Item removed from cart!');
        location.reload(); 
    }
});
