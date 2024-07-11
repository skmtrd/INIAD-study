// Problem
function calcTax() {
  let priceInput = document.getElementById("price-without-tax");
  let taxInput = document.getElementById("tax-rate");

  let price = Number(priceInput.value);
  let tax = Number(taxInput.value);

  let taxAmount = price * (tax / 100);
  let priceWithTax = price + taxAmount;

  let priceWithTaxElement = document.getElementById("price");
  let taxAmountElement = document.getElementById("tax");

  priceWithTaxElement.textContent = String(priceWithTax);
  taxAmountElement.textContent = String(taxAmount);
}
