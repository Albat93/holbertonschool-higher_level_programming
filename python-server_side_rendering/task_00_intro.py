import os


def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check for empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        personalized = template
        for key in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            personalized = personalized.replace(f"{{{key}}}", str(value))

        # Write to output file
        filename = f"output_{i}.txt"
        try:
            with open(filename, "w") as f:
                f.write(personalized)
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")
