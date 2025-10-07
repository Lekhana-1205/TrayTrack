# Path: src/models/report.py
class Report:
    def __init__(self, total_waste, notes, created_at):
        self.total_waste = total_waste
        self.notes = notes
        self.created_at = created_at

    def __repr__(self):
        return f"<Report TotalWaste:{self.total_waste}, Notes:{self.notes}, Date:{self.created_at}>"
