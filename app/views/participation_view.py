def show_participants(olympiad_id, participants):
    if not participants:
        print("Нет участников.")
        return
    print(f"\nУЧАСТНИКИ ОЛИМПИАДЫ (ID: {olympiad_id})")
    print("-" * 40)
    for p in participants:
        print(f"• ID:{p['id']:2} {p['student_name']}")