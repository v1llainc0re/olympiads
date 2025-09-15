def show_olympiads(olympiads):
    if not olympiads:
        print("Нет олимпиад.")
        return
    print("\nСПИСОК ОЛИМПИАД")
    print("-" * 60)
    print(f"{'ID':<4} {'Год':<6} {'Название':<30} {'Период':<20}")
    print("-" * 60)
    for o in olympiads:
        period = f"{o['start_date']} — {o['end_date']}"
        print(f"{o['id']:<4} {o['year']:<6} {o['title']:<30} {period:<20}")


def show_olympiad_details(olympiad):
    print(f"\nДЕТАЛИ ОЛИМПИАДЫ: {olympiad['title']}")
    print("-" * 50)
    print(f"Год:            {olympiad['year']}")
    print(f"Период:         {olympiad['start_date']} — {olympiad['end_date']}")