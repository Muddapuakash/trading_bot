import argparse
import sys

from bot.orders import OrderService
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate the order without placing it"
    )

    args = parser.parse_args()

    try:
        # Validation
        validate_symbol(args.symbol)
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.price, args.type)

        print("\n================ ORDER REQUEST ================")
        print(f"Symbol     : {args.symbol}")
        print(f"Side       : {args.side}")
        print(f"Type       : {args.type}")
        print(f"Quantity   : {args.quantity}")
        if args.type == "LIMIT":
            print(f"Price      : {args.price}")
        print("==============================================\n")

        # ✅ DRY RUN MODE (CORRECT PLACE)
        if args.dry_run:
            print("🟡 DRY RUN MODE ENABLED")
            print("No order was sent to Binance.")
            print("All inputs validated successfully.\n")
            sys.exit(0)

        orders = OrderService()

        # Route order
        if args.type == "MARKET":
            response = orders.place_market_order(
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity
            )
        else:
            response = orders.place_limit_order(
                symbol=args.symbol,
                side=args.side,
                quantity=args.quantity,
                price=args.price
            )

        # Output response
        print("=============== ORDER RESPONSE ===============")
        print("Order ID      :", response.get("orderId"))
        print("Status        :", response.get("status"))
        print("Executed Qty  :", response.get("executedQty"))
        print("Avg Price     :", response.get("avgPrice", "N/A"))
        print("==============================================\n")

        print("✅ Order executed successfully!")

    except Exception as e:
        print("\n❌ ERROR:", str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
