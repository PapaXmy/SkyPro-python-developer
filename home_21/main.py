from store_shop_classes import Shop, Store, Request


def main(store, shop) -> None:

    while True:
        request_str = input("Введите запрос, для выхода введите 'в': ")
        if request_str.lower() == "в":
            break

        request = Request(request_str)

        if store.get_items()[request.product] >= request.amount:

            if shop.capacity >= request.amount and shop.get_unique_items_count() < 5:
                store.remove(request.product, request.amount)
                print("Нужное количество есть на складе")

                print(
                    f"Курьер забрал {request.amount} {request.product} со {
                        request.from_}"
                )
                print(
                    f"Курьер везет {request.amount} {request.product} со {
                        request.from_} в {request.to}"
                )
                print(
                    f"Курьер доставил {request.amount} {request.product} в {
                        request.to}"
                )
                shop.add(request.product, request.amount)
                print(f"\nВ {request.from_} хранится:\n")

                for item, quantity in store.get_items().items():
                    print(f"{quantity} {item}")

                print("\nВ магазин хранится:\n")
                print(f"{shop.capacity}")

                for item, quantity in shop.get_items().items():
                    print(f"{quantity} {item}")
            else:
                print("В магазине не хватает места, попробуйте что то другое")
        else:
            print("Товара не хватает на складе, попробуйте заказать меньше")


if __name__ == "__main__":
    store = Store()
    store.add("печеньки", 5)
    store.add("яблоки", 5)
    store.add("мандарины", 5)
    store.add("апельсины", 5)
    store.add("вафли", 5)
    store.add("бананы", 5)
    shop = Shop()
    main(store, shop)
