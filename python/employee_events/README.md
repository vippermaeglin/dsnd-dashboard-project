Diagram

  employee {
    INTEGER index
    INTEGER employee_id
    TEXT first_name
    TEXT last_name
    INTEGER team_id
  }

  employee_events {
    INTEGER index
    TEXT event_date
    INTEGER employee_id
    INTEGER team_id
    INTEGER positive_events
    INTEGER negative_events
  }

  notes {
    INTEGER index
    INTEGER employee_id
    INTEGER team_id
    TEXT note
    TEXT note_date
  }

  team {
    INTEGER index
    INTEGER team_id
    TEXT team_name
    TEXT shift
    TEXT manager_name
  }

