import React from 'react';
import { 
  Card, 
  CardContent, 
  List, 
  ListItem, 
  ListItemText, 
  Typography, 
  IconButton,
  Chip,
  Divider
} from '@mui/material';
import { Notifications, Close } from '@mui/icons-material';

const AlertsPanel = ({ priceAlerts, onDismissAlert }) => {
  return (
    <Card elevation={3}>
      <CardContent>
        <Typography variant="h6" gutterBottom sx={{ display: 'flex', alignItems: 'center' }}>
          <Notifications color="primary" sx={{ mr: 1 }} />
          Price Alerts
        </Typography>
        <Divider sx={{ mb: 2 }} />
        
        {priceAlerts?.length > 0 ? (
          <List dense>
            {priceAlerts.map((alert) => (
              <ListItem
                key={alert.id}
                secondaryAction={
                  <IconButton edge="end" onClick={() => onDismissAlert(alert.id)}>
                    <Close />
                  </IconButton>
                }
              >
                <ListItemText
                  primary={
                    <>
                      <Chip 
                        label={alert.severity} 
                        size="small" 
                        color={alert.severity === 'High' ? 'error' : 'warning'}
                        sx={{ mr: 1 }}
                      />
                      {alert.item}
                    </>
                  }
                  secondary={`${alert.message} - ${new Date(alert.timestamp).toLocaleTimeString()}`}
                />
              </ListItem>
            ))}
          </List>
        ) : (
          <Typography variant="body2" color="text.secondary" align="center">
            No active alerts
          </Typography>
        )}
      </CardContent>
    </Card>
  );
};

export default AlertsPanel;