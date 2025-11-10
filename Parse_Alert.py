import json

# CRITIQUE : Définir les booléens JavaScript pour Python
true = True
false = False
null = None

# Maintenant on peut utiliser $exec sans erreur
data = $exec

# Extraire all_fields
af = data.get("all_fields", {})
r = af.get("rule", {})
a = af.get("agent", {})
d = af.get("data", {})

# Résultat
result = {
    "rule_id": str(r.get("id", "unknown")),
    "rule_description": str(r.get("description", "Unknown")),
    "rule_level": int(r.get("level", 10)),
    "source_ip": str(d.get("srcip", "0.0.0.0")),
    "target_agent": str(a.get("name", "unknown")),
    "target_ip": str(a.get("ip", "0.0.0.0")),
    "attempted_user": str(d.get("dstuser", "unknown")),
    "timestamp": str(af.get("timestamp", "2025-10-28"))
}

print(json.dumps(result))
