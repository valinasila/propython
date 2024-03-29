import gobject
import gtk
import appindicator

if __name__ == "__main__":

  def menuitem_response(w, buf):
    if ind.get_status() == appindicator.STATUS_ATTENTION:
      ind.set_status(appindicator.STATUS_ACTIVE)
    else:
      ind.set_status(appindicator.STATUS_ATTENTION)

  ind = appindicator.Indicator("example-simple-client",
                              "indicator-messages",
                              appindicator.CATEGORY_APPLICATION_STATUS)
  ind.set_status(appindicator.STATUS_ACTIVE)
  ind.set_attention_icon("indicator-messages-new")

  # create a menu
  menu = gtk.Menu()

  # create some 
  for i in range(3):
    buf = "Test-undermenu - %d" % i

    menu_items = gtk.MenuItem(buf)

    menu.append(menu_items)

    # this is where you would connect your menu item up with a function:
    
    menu_items.connect("activate", menuitem_response, buf)

    # show the items
    menu_items.show()

  ind.set_menu(menu)


  gtk.main()