import pytest

def process_payment(payment_gateway, amount):
    responce = payment_gateway.charge(amount)

    if responce == 'Success':
        return "Payment processed successfully"
    else:
        raise ValueError("Payment failed")


def test_process_payment(mocker):
    mock_payment_gateway = mocker.Mock()

    mock_payment_gateway.charge.side_effect = ['Success', ValueError("Insufficient funds")]

    responce = process_payment(mock_payment_gateway, 100)

    assert responce == 'Payment processed successfully'

    with pytest.raises(ValueError, match='Insufficient funds'):
        process_payment(mock_payment_gateway, 200)

    assert mock_payment_gateway.charge.call_count == 2    