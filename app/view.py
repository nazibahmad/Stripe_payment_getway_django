def charge(request):
    stripe.api_key = "pk_test_6pRNASCoBOKtIshFeQd4XMUh"

# Token is created using Stripe.js or Checkout!
# Get the payment token submitted by the form:
    token = request.POST['stripeToken']

# Create a Customer:
    customer = stripe.Customer.create(
     email="paying.user@example.com",
     source=token,
    )

# Charge the Customer instead of the card:
    charge = stripe.Charge.create(
     amount="1000",
     currency="usd",
     customer=customer.id,
    )


    return render(request,'stripe.html')
