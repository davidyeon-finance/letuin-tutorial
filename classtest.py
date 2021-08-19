class VC:
  def __init__(self, player, uniform):
    self.player = player
    self.uniform = uniform

  def kick(self):
    print(self.player + ' kick ' + self.uniform)

  def goal(self):
    print(self.player + 'goal')

a_soccer_player = SoccerPlayers(player = 'messi', uniform = 'paris')
a_soccer_player.kick()