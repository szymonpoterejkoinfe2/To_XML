
class Transaction:
    def __init__(this, isRefund,transactionIdentifier,dateTime,transactionDateType,amount,currency,paymentMethodType,initiatedAtPhysicalPremisesOfMerchant,payerMS, payerMSSource):
        this.isRefund = isRefund
        this.transactionIdentifier = transactionIdentifier
        this.dateTime = dateTime
        this.transactionDateType = transactionDateType
        this.amount = amount
        this.currency = currency
        this.paymentMethodType = paymentMethodType
        this.initiatedAtPhysicalPremisesOfMerchant = initiatedAtPhysicalPremisesOfMerchant
        this.payerMS = payerMS
        this.payerMSSource = payerMSSource