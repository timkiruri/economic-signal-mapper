"use client"

import { Alert } from '@/lib/api'
import { Badge } from '@/components/ui/badge'
import { TrendingUp, TrendingDown } from 'lucide-react'

interface RecentAlertsProps {
  alerts: Alert[]
}

export function RecentAlerts({ alerts }: RecentAlertsProps) {
  if (alerts.length === 0) {
    return (
      <div className="text-center py-8 text-muted-foreground">
        No recent alerts
      </div>
    )
  }

  return (
    <div className="space-y-4">
      {alerts.map((alert) => (
        <div key={alert.id} className="flex items-center justify-between p-3 border rounded-lg">
          <div className="flex items-center space-x-3">
            {alert.direction === 'increase' ? (
              <TrendingUp className="h-4 w-4 text-red-500" />
            ) : (
              <TrendingDown className="h-4 w-4 text-green-500" />
            )}
            <div>
              <p className="text-sm font-medium">{alert.description}</p>
              <p className="text-xs text-muted-foreground">
                {new Date(alert.timestamp).toLocaleDateString()}
              </p>
            </div>
          </div>
          <div className="text-right">
            <Badge variant={alert.direction === 'increase' ? 'destructive' : 'default'}>
              {alert.direction === 'increase' ? '+' : '-'}
              KES {Math.abs(alert.price_change).toFixed(2)}
            </Badge>
          </div>
        </div>
      ))}
    </div>
  )
}
