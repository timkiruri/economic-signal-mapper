"use client"

import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { cn } from '@/lib/utils'
import { BarChart3, Package, Store, TrendingUp, Home} from 'lucide-react'

const navigation = [
  { name: 'Dashboard', href: '/', icon: Home },
  { name: 'Products', href: '/products', icon: Package },
  { name: 'Retailers', href: '/retailers', icon: Store },
  { name: 'Forecasting', href: '/forecast', icon: TrendingUp }
]

export function Sidebar() {
  const pathname = usePathname()

  return (
    <div className="w-64 bg-card border-r border-border">
      <div className="p-6">
        <h1 className="text-2xl font-bold text-foreground">BeiWatch</h1>
        <p className="text-sm text-muted-foreground">Retail Price Monitor</p>
      </div>
      
      <nav className="px-4 space-y-2">
        {navigation.map((item) => {
          const isActive = pathname === item.href
          return (
            <Link
              key={item.name}
              href={item.href}
              className={cn(
                "flex items-center px-3 py-2 rounded-md text-sm font-medium transition-colors",
                isActive
                  ? "bg-primary text-primary-foreground"
                  : "text-muted-foreground hover:text-foreground hover:bg-accent"
              )}
            >
              <item.icon className="mr-3 h-4 w-4" />
              {item.name}
            </Link>
          )
        })}
      </nav>
    </div>
  )
}
