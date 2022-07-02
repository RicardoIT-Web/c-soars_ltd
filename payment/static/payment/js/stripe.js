let stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1)
let client_secret = $('#id_client_secret').text().slice(1, -1)
let stripe = Stripe(stripe_public_key);
let elements = stripe.elements();
let card = elements.create('card');

let style = {
    base: {
        color: '#050f56',
        fontFamily: '',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

card.mount('#card-element', {style:style});