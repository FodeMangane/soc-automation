Étape 1 : Création de l'application Slack
   1. Accéder à https://api.slack.com/apps
   2. Cliquer sur Create New App
   3. Sélectionner From scratch
   4. Remplir : 
      App Name : SOC Bot
      Workspace : Sélectionner votre workspace Slack
   5. Puis nous clicons sur notre App
![Création de l'application SOC Bot](images/slack1.png)

Étape 2 : Configuration des permissions (OAuth Scopes)
  1.	Dans le menu de gauche, aller dans OAuth & Permissions
  2.	Descendre jusqu'à Scopes → Bot Token Scopes
  3.	Cliquer sur Add an OAuth Scope
  4.	Ajouter les permissions suivantes : 
  o	chat:write : Pour envoyer des messages
  o	channels:read : Pour lire les informations des canaux

Étape 3 : Installation du Bot dans le workspace
  1.	Remonter en haut de la page OAuth & Permissions
  2.	Cliquer sur Install to Workspace
  3.	Autoriser les permissions demandées
  4.	COPIER LE TOKEN qui commence par xoxb- (Bot User OAuth Token)
![Configuration des permissions](images/slack2.png)

Étape 4 : Création du canal et ajout du bot
1.	Dans votre workspace Slack, créer un nouveau canal : #soc-alerts
2.	Dans le canal, taper /invite @SOC Bot pour ajouter le bot au canal
3.	Le bot doit apparaître dans la liste des membres du canal
![Bot User OAuth Token](images/slack3.png)

Body :

{
  "channel": "#soc-alerts",
  "text": "🚨 *WAZUH ALERT - SSH Brute Force Detected* 🚨\n\n*Rule:* $parse_alert.message.rule_id - $parse_alert.message.rule_description\n*Severity:* $parse_alert.message.rule_level\n*Source IP:* $parse_alert.message.source_ip\n*Target:* $parse_alert.message.target_agent ($parse_alert.message.target_ip)\n*User:* $parse_alert.message.attempted_user\n*Time:* $parse_alert.message.timestamp\n\n📊 *Actions Taken:*\n✅ TheHive Case Created\n✅ MISP Event #$misp_create_event.body.Event.id Created\n✅ IP Added to MISP IoC\n✅ IP Blocked\n\n🔗 *Links:*\nTheHive: http://10.0.30.104:9003\MISP: http://10.0.30.104/events/view/$misp_create_event.body.Event.id",
  "mrkdwn": true
}
